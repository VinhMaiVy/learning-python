#!/bin/python3

"""
AWS Lambda
    def lambda_handler(event, context)

    def query_mac_addr_bank(dynamodb=None)
    def insert_mac_addr_bank(addr_start: str, count: int,
                userid: str, dynamodb=None) -> int
    def update_mac_addr_bank(reserve: int, userid: str, dynamodb=None) -> str
    def insert_mac_addr_log(userid: str, command: str, addr_start:
                            str, count: int, status: int, dynamodb=None) -> int

    def create_mac_addr_bank_table(dynamodb=None)
    def create_mac_addr_log_table(dynamodb=None)

DynamoDB
    mac_addr_bank table
    mac_addr_log table

Command line:
    curl 'https://r4ctlbqq0b.execute-api.us-east-2.amazonaws.com/
        test?command=QUERY_LOG' | jq

"""
import re
import boto3
# import time
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from decimal import Decimal
from datetime import datetime


# Check if a string is a correct MAC address
def is_mac_str(h: str):
    return 1 if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){6}$",
                         h.lower()) else 0


# Convert MAC address to int
def mac_hex_to_int(h: str) -> int:
    h = h.replace(':', '')
    h = int(h, 16)
    return h


# Convert int to MAC address
def int_to_mac_hex(i: int) -> str:
    i = str(hex(i).lstrip("0x"))
    i = i.upper()
    return ":".join(i[_i:_i + 2] for _i in range(0, len(i), 2))


# Reserver a range of MAC addresses
def reserve_range_addr(addr_start_hex: str,
                       current_remain: int, reserve: int) -> str:

    if is_mac_str(addr_start_hex):
        addr_start_int = mac_hex_to_int(addr_start_hex) + \
            current_remain - reserve

        return int_to_mac_hex(addr_start_int)
    else:
        return '00:00:00:00:00:00:00:00'


def update_mac_addr_bank(reserve: int, userid: str, dynamodb=None) -> str:
    '''
     Updating MAC_ADDR_BANK_TABLE
    '''

    global MAC_ADDR_BANK_TABLE

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    tstamp = str(datetime.utcnow().isoformat())

    '''
    mac_addr_bank SCAN
    '''
    table = dynamodb.Table(MAC_ADDR_BANK_TABLE)

    response = table.scan(
            FilterExpression=Attr('remain').gte(reserve),
            ConsistentRead=True
            )

    available_ranges = response['Items']
    '''
    Find the smallest available address range
    '''
    if available_ranges:
        min_available_range = min(available_ranges, key=lambda i: i['remain'])
    else:
        return '00:00:00:00:00:00:00:00'

    addr_start = min_available_range['addr_start']
    init_range = min_available_range['init_range']
    current_remain = int(min_available_range['remain'])
    min_tstamp = min_available_range['tstamp']

    # time.sleep(1)

    '''
    mac_addr_bank UPDATE
    '''
    try:
        response = table.update_item(
            Key={
                'addr_start': addr_start,
                'init_range': init_range
            },
            UpdateExpression="set remain=:r, tstamp=:t, userid=:u",
            ConditionExpression="tstamp = :mt",  # Make sure the data
            ExpressionAttributeValues={  # updated is the data read
                ':r': Decimal(current_remain - reserve),
                ':t': tstamp,
                ':mt': min_tstamp,
                ':u': userid
            },
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as _:
        return '00:00:00:00:00:00:00:00'
    else:
        return reserve_range_addr(addr_start, current_remain, reserve)


def insert_mac_addr_bank(addr_start: str, count: int,
                         userid: str, dynamodb=None) -> int:
    '''
     Inserting to MAC_ADDR_BANK_TABLE
    '''

    global MAC_ADDR_BANK_TABLE
    global ERROR429
    global ERROR500

    if not is_mac_str(addr_start):
        return(ERROR500)  # Bad Request Body

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    tstamp = str(datetime.utcnow().isoformat())

    table = dynamodb.Table(MAC_ADDR_BANK_TABLE)

    response = table.query(
        KeyConditionExpression=Key('addr_start').eq(addr_start)
    )

    if response['Count'] != 0:
        return (ERROR429)  # Addr_start already exist

    response = table.put_item(
       Item={
            'addr_start': addr_start,
            'init_range': count,
            'remain': count,
            'userid': userid,
            'tstamp': tstamp
        }
    )
    return response['ResponseMetadata']['HTTPStatusCode']


def insert_mac_addr_log(userid: str, command: str, addr_start: str,
                        count: int, status: int, dynamodb=None) -> int:

    '''
     Inserting to MAC_ADDR_LOG_TABLE
    '''

    global MAC_ADDR_LOG_TABLE
    global ERROR400

    if not is_mac_str(addr_start):
        return(ERROR400)  # Bad Request Body

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    tstamp = str(datetime.utcnow().isoformat())

    table = dynamodb.Table(MAC_ADDR_LOG_TABLE)
    response = table.put_item(
       Item={
            'userid': userid,
            'tstamp': tstamp,
            'command': command,
            'addr_start': addr_start,
            'count': count,
            'status': status
        }
    )
    return response['ResponseMetadata']['HTTPStatusCode']


def query_mac_addr_bank(dynamodb=None):

    global MAC_ADDR_BANK_TABLE

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(MAC_ADDR_BANK_TABLE)

    response = table.scan()

    available_ranges = response['Items']
    sum_remain = 0
    for available_range in available_ranges:
        sum_remain += int(available_range['remain'])
    return sum_remain


def query_mac_addr_logs(userid: str, dynamodb=None):

    global MAC_ADDR_LOG_TABLE

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(MAC_ADDR_LOG_TABLE)

    response = table.query(
        KeyConditionExpression=Key('userid').eq(userid)
    )

    logs = response['Items']
    return logs


def create_mac_addr_bank_table(dynamodb=None):

    global MAC_ADDR_BANK_TABLE
    global RETURNOK

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    try:
        _ = dynamodb.create_table(
            TableName=MAC_ADDR_BANK_TABLE,
            KeySchema=[
                {
                    'AttributeName': 'addr_start',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'init_range',
                    'KeyType': 'RANGE'  # Sort key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'addr_start',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'init_range',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except Exception as err:
        return err
    else:
        return RETURNOK


def create_mac_addr_log_table(dynamodb=None):

    global MAC_ADDR_LOG_TABLE
    global RETURNOK

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    try:
        _ = dynamodb.create_table(
            TableName=MAC_ADDR_LOG_TABLE,
            KeySchema=[
                {
                    'AttributeName': 'userid',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'tstamp',
                    'KeyType': 'RANGE'  # Sort key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'userid',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'tstamp',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except Exception as err:
        return err
    else:
        return RETURNOK


def lambda_handler(event, context):

    global MAC_ADDR_BANK_TABLE
    global MAC_ADDR_LOG_TABLE

    global ERROR400
    global ERROR429
    global ERROR500
    global RETURNOK  # do not change

    ERROR400 = 400
    ERROR429 = 429
    ERROR500 = 500
    RETURNOK = 200

    context = event['context']
    params = event['params']
    querystring = params['querystring']

    stage = context['stage']
    userid = context['source-ip']
    resource_path = context['resource-path']

    if 'addr_start' in querystring:
        addr_start = querystring['addr_start']
    else:
        addr_start = '00:00:00:00:00:00:00:00'

    if 'count' in querystring:
        count = int(querystring['count'])
    else:
        count = 0

    command = resource_path[1:]

    tstart = str(datetime.utcnow().isoformat())

    if stage == 'beta':
        MAC_ADDR_BANK_TABLE = 'mac_addr_bank.beta'
        MAC_ADDR_LOG_TABLE = 'mac_addr_log.beta'
    elif stage in ('test', 'test-invoke-stage'):
        MAC_ADDR_BANK_TABLE = 'mac_addr_bank.test'
        MAC_ADDR_LOG_TABLE = 'mac_addr_log.test'
    elif stage == 'prod':
        MAC_ADDR_BANK_TABLE = 'mac_addr_bank.prod'
        MAC_ADDR_LOG_TABLE = 'mac_addr_log.prod'
    else:
        MAC_ADDR_BANK_TABLE = 'mac_addr_bank.test'
        MAC_ADDR_LOG_TABLE = 'mac_addr_log.test'

    if command == 'reserve-mac':
        if count:
            addr_start = update_mac_addr_bank(count, userid)
        if addr_start != '00:00:00:00:00:00:00:00':
            msg = "MAC address range reserved successfully."
            ret = RETURNOK
        else:
            msg = "MAC address range reserve failure."
            ret = ERROR400

        insert_mac_addr_log(userid, command, addr_start, count, ret)
        tend = str(datetime.utcnow().isoformat())
        return {
                'statusCode': ret,
                'body': {"Msg": msg, "command": command,
                         "addr_start": addr_start, "count": count,
                         "tstart": tstart, "tend": tend}
                }

    elif command in ('return-mac', 'set-mac'):
        if addr_start and count:
            ret = insert_mac_addr_bank(addr_start, count, userid)
        else:
            ret = ERROR400

        if (ret == RETURNOK):
            msg = "MAC address range set/returned successfully."
        else:
            ret = ERROR400
            msg = "MAC address range set/returned failed."

        insert_mac_addr_log(userid, command, addr_start, count, ret)
        tend = str(datetime.utcnow().isoformat())
        return {
                'statusCode': ret,
                'body': {"Msg": msg, "command": command,
                         "addr_start": addr_start, "count": count,
                         "tstart": tstart, "tend": tend}
                }

    elif command == 'query-mac':
        sum_remain = query_mac_addr_bank()
        tend = str(datetime.utcnow().isoformat())
        return {
                'statusCode': RETURNOK,
                'body': {"command": command, "remain": sum_remain,
                         "tstart": tstart, "tend": tend}
                }

    elif command == 'query-log':
        logs = query_mac_addr_logs(userid)
        return logs

    elif command == 'create-table':
        tstart = str(datetime.utcnow().isoformat())
        ret1 = create_mac_addr_bank_table()
        tend = str(datetime.utcnow().isoformat())
        if ret1 == RETURNOK:
            return {
                        'statusCode': ERROR400,
                        'body': {"Msg": ret1, "command": command,
                                 "tstart": tstart, "tend": tend}
                    }
        ret2 = create_mac_addr_log_table()
        tend = str(datetime.utcnow().isoformat())
        if ret2 == RETURNOK:
            return {
                        'statusCode': ERROR400,
                        'body': {"Msg": ret2, "command": command,
                                 "tstart": tstart, "tend": tend}
                    }

        tend = str(datetime.utcnow().isoformat())
        return {
                    'statusCode': RETURNOK,
                    'body': {"Msg": "Table created successfully.",
                             "command": command, "tstart": tstart,
                             "tend": tend}
                }


if __name__ == '__main__':
    global MAC_ADDR_BANK_TABLE
    global MAC_ADDR_LOG_TABLE

    MAC_ADDR_BANK_TABLE = 'mac_addr_bank'
    MAC_ADDR_LOG_TABLE = 'mac_addr_log'

    global ERROR400
    global ERROR429
    global ERROR500
    global RETURNOK  # do not change

    ERROR400 = 400
    ERROR429 = 429
    ERROR500 = 500
    RETURNOK = 200

    event = {
        'params': {
                'querystring': {
                    #    'addr_start': 'C4:98:A6:00:00:00:00:00',
                    #    'addr_start': 'C4:98:A8:00:00:00:00:00',
                    #    'addr_start': 'C4:98:A6:00:00:00:00:00',
                    'addr_start': 'C4:98:A5:00:00:00:00:00',
                    'count': 10
                    }
        },
        'context': {
            'source-ip': '108.253.242.242',
            'stage': 'test',
            #    'stage': 'beta'
            #    'stage': 'test'
            #    'stage': 'prod'
            #    "resource-path": "/query-mac"
            #    "resource-path": "/reserve-mac"
            #    "resource-path": "/return-mac"
            #    "resource-path": "/set-mac"
            #    "resource-path": "/query-log"
            #    "resource-path": "/create-table"
            "resource-path": "/query-mac"
            }
        }
    context = ''

    print(lambda_handler(event, context))
