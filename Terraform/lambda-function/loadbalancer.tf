resource "aws_lambda_permission" "echo" {
  statement_id  = "AllowExecutionFromlb"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.echo.arn
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.echo.arn
}

resource "aws_lb" "echo" {
  name = "echo"
  internal = false
  load_balancer_type = "application"
  security_groups = [ aws_security_group.echo-lb.id ]
  subnets = [aws_subnet.echo-a.id, aws_subnet.echo-b.id]

  access_logs {
    bucket  = aws_s3_bucket.echo.bucket
    prefix  = "ec2"
    enabled = true
  }
}

resource "aws_lb_target_group" "echo" {
  name     = "echo"
  port     = var.trg_port
  protocol = var.trg_proto
  target_type = "lambda"
}

resource "aws_lb_listener" "echo" {
  load_balancer_arn = aws_lb.echo.arn
  port              = var.src_port
  protocol          = var.src_proto

 default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.echo.arn
  }
}

resource "aws_lb_target_group_attachment" "echo" {
  target_group_arn = aws_lb_target_group.echo.arn
  target_id        = aws_lambda_function.echo.arn
  depends_on       = [aws_lambda_permission.echo]
}
