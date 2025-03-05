alarm_to_slack_lambda = lambda_.Function(
    self,
    id='AlarmToSlackLambda',
    runtime=lambda_.Runtime.PYTHON_3_8,
    code=lambda_.Code.from_asset('lib/'),
    handler='index.lambda_handler',
    environment={'SLACK_WEBHOOK_URL': 'https://hooks.slack.com/services/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'}
)