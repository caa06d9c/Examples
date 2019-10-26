resource "aws_lb_listener_rule" "echo-200" {
  listener_arn  = aws_lb_listener.echo.arn
  priority      = 100

  action {
    type = "forward"
    target_group_arn = aws_lb_target_group.echo.arn
  }

  condition {
    field = "host-header"
    values = [var.domain_200]
  }
}

resource "aws_lb_listener_rule" "echo-500" {
  listener_arn  = aws_lb_listener.echo.arn

  action {
    type = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      message_body = "echo-500"
      status_code = "500"
    }
  }

  condition {
    field = "host-header"
    values = [var.domain_500]
  }
}
