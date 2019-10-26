# basic
variable "region" { default = "us-east-1" }

# vpc
variable "vpc_name" { default = "echo" }
variable "cidr_block" {default = "192.168.0.0/16"}
variable "subnet_a" { default = "192.168.1.0/24" }
variable "subnet_b" { default = "192.168.2.0/24" }

# autoscaling
variable "min_size" { default = 2}
variable "max_size" { default = 5}
variable "name" { default = "echo" }
variable "type" { default = "webserver" }

# alb
variable "src_port" { default = 80 }
variable "trg_port" { default = 80 }
variable "src_proto" { default = "HTTP" }
variable "trg_proto" { default = "HTTP" }
variable "timeout" { default = 3}
variable "interval" { default = 15 }
variable "threshold_healthy" { default = 2 }
variable "threshold_unhealthy" { default = 2 }
variable "domain_200" { default = "echo200.demin.co" }
variable "domain_500" { default = "echo500.demin.co" }
variable "s3_bucket" {default = "echo-caa06d9c" }

