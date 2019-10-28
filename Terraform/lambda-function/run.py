from json import dumps
from logging import info, getLogger, INFO

logger = getLogger()
logger.setLevel(INFO)


def run(event, context):

    result = {'method': event['httpMethod'],
              'path': event['path'],
              'ip': event['headers']['x-forwarded-for'],
              'host': event['headers']['host'],
              'headers': dict()}

    for header in ['x-forwarded-port','x-forwarded-proto']:
        result['headers'][header] = event['headers'][header]

    logger.info(result)

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'statusDescription': '200 OK',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': dumps(result, indent=4)
    }
