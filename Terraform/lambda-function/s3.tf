resource "aws_s3_bucket" "echo" {
  bucket = var.s3_bucket
  acl    = "private"

  tags = {
    Name = "echo"
  }
  policy = <<POLICY
{
    "Id": "Policy1571451924952",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "1",
            "Action": [
                "s3:PutObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::${var.s3_bucket}/*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::127311923021:root"
                ]
            }
        }
    ]
}
  POLICY
}
