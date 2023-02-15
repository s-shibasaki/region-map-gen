# RegionMap Generator

Automatically creates a RegionMap of EC2 ImageId for CloudFormation templates.

## Usage

```
python main.py --image-name "Deep Learning AMI GPU PyTorch 1.13.1 (Ubuntu 20.04) 20230208"
```

Sample output:

```
17 regions are available.
Image ID for region ap-south-1 is ami-0d5970bd311ec8f6d.
Image ID for region eu-north-1 is ami-03d5696c7f0d9b8d1.
Image ID for region eu-west-3 is ami-085f3555d6f6b9b30.
Image ID for region eu-west-2 is ami-0f7efbcc7df39f6f1.
Image ID for region eu-west-1 is ami-0a532245f05a1badd.
Image ID for region ap-northeast-3 is ami-066ec32514094dcba.
Image ID for region ap-northeast-2 is ami-09de3835c13000002.
Image ID for region ap-northeast-1 is ami-0e962d4dc5fafc64a.
Image ID for region ca-central-1 is ami-0ce02fc9b733884dc.
Image ID for region sa-east-1 is ami-0c52ad992252fc79b.
Image ID for region ap-southeast-1 is ami-0a92f17faa3a6b301.
Image ID for region ap-southeast-2 is ami-0253ebbef57ef7291.
Image ID for region eu-central-1 is ami-098f065ef7d1a9f50.
Image ID for region us-east-1 is ami-0434abb28cf6cc2b1.
Image ID for region us-east-2 is ami-03659a8622ebc7edc.
Image ID for region us-west-1 is ami-0eefe72da2b4ee5a8.
Image ID for region us-west-2 is ami-0a81b127856035c77.
The result json is shown below.
{
  "RegionMap": {
    "ap-south-1": {
      "ImageId": "ami-0d5970bd311ec8f6d"
    },
    "eu-north-1": {
      "ImageId": "ami-03d5696c7f0d9b8d1"
    },
    "eu-west-3": {
      "ImageId": "ami-085f3555d6f6b9b30"
    },
    "eu-west-2": {
      "ImageId": "ami-0f7efbcc7df39f6f1"
    },
    "eu-west-1": {
      "ImageId": "ami-0a532245f05a1badd"
    },
    "ap-northeast-3": {
      "ImageId": "ami-066ec32514094dcba"
    },
    "ap-northeast-2": {
      "ImageId": "ami-09de3835c13000002"
    },
    "ap-northeast-1": {
      "ImageId": "ami-0e962d4dc5fafc64a"
    },
    "ca-central-1": {
      "ImageId": "ami-0ce02fc9b733884dc"
    },
    "sa-east-1": {
      "ImageId": "ami-0c52ad992252fc79b"
    },
    "ap-southeast-1": {
      "ImageId": "ami-0a92f17faa3a6b301"
    },
    "ap-southeast-2": {
      "ImageId": "ami-0253ebbef57ef7291"
    },
    "eu-central-1": {
      "ImageId": "ami-098f065ef7d1a9f50"
    },
    "us-east-1": {
      "ImageId": "ami-0434abb28cf6cc2b1"
    },
    "us-east-2": {
      "ImageId": "ami-03659a8622ebc7edc"
    },
    "us-west-1": {
      "ImageId": "ami-0eefe72da2b4ee5a8"
    },
    "us-west-2": {
      "ImageId": "ami-0a81b127856035c77"
    }
  }
}
```
