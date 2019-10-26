data "template_file" "userdata" {
  template = file("userdata.tpl")
  vars = {
    app_version = var.app_version
  }
}

resource "aws_launch_configuration" "echo" {
  image_id = var.ami
  instance_type = var.instance_type
  key_name = var.key_name
  security_groups = [ aws_security_group.echo-instances.id ]
  user_data = data.template_file.userdata.rendered
  associate_public_ip_address = true
}

resource "aws_autoscaling_group" "echo" {
  name = "echo"
  health_check_type = "ELB"
  launch_configuration = aws_launch_configuration.echo.id
  target_group_arns = [aws_lb_target_group.echo.arn]
  max_size = var.max_size
  min_size = var.min_size
  vpc_zone_identifier = [aws_subnet.echo-a.id, aws_subnet.echo-b.id]

  lifecycle {
    create_before_destroy = true
  }

  tag {
    key = "Name"
    value = var.name
    propagate_at_launch = true
  }

  tag {
    key = "Type"
    value = var.type
    propagate_at_launch = true
  }
}
