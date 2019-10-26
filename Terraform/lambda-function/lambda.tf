resource "aws_iam_role" "echo" {
  name = "echo"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "echo" {
  filename      = "run.py.zip"
  function_name = "echo"
  role          = aws_iam_role.echo.arn
  handler       = "run.run"

  runtime = "python3.7"
}