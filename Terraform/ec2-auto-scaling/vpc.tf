provider "aws" {
  region = var.region
}

resource "aws_vpc" "echo" {
  cidr_block = var.cidr_block
  tags = {
    Name = "echo"
  }
}

resource "aws_internet_gateway" "echo" {
  vpc_id = aws_vpc.echo.id

  tags = {
    Name = "echo"
  }
}

resource "aws_route_table" "echo" {
  vpc_id = aws_vpc.echo.id
  tags = {
    Name = "echo"
  }

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.echo.id
  }
}

resource "aws_subnet" "echo-a" {
  vpc_id = aws_vpc.echo.id
  availability_zone = "${var.region}a"
  cidr_block        = var.subnet_a
  tags = {
    Name = "echo-a"
  }
}

resource "aws_subnet" "echo-b" {
  vpc_id = aws_vpc.echo.id
  availability_zone = "${var.region}b"
  cidr_block = var.subnet_b
  tags = {
    Name = "echo-b"
  }
}

resource "aws_route_table_association" "echo-a" {
  subnet_id      = aws_subnet.echo-a.id
  route_table_id = aws_route_table.echo.id
}

resource "aws_route_table_association" "echo-b" {
  subnet_id      = aws_subnet.echo-b.id
  route_table_id = aws_route_table.echo.id
}
