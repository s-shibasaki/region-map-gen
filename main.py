import json
import logging

import boto3
import click


logger = logging.getLogger(__name__)


@click.command()
@click.option("--image-name")
def main(image_name):
    available_regions = get_available_regions()
    print("{} regions are available.".format(len(available_regions)))

    result = {"RegionMap": {}}

    for region in available_regions:
        image_id = get_image_id_by_name(image_name, region)

        if image_id:
            print("Image ID for region {} is {}.".format(region, image_id))
            result["RegionMap"][region] = {"ImageId": image_id}

    result_json = json.dumps(result, indent=2)
    print("The result json is shown below.")
    print(result_json)


def get_available_regions():
    client = boto3.client("ec2")
    response = client.describe_regions()

    logger.debug("Response for describe_regions: {}".format(response))

    return [region["RegionName"] for region in response["Regions"]]


def get_image_id_by_name(image_name, region):
    client = boto3.client("ec2", region_name=region)
    response = client.describe_images(
        Filters=[{"Name": "name", "Values": [image_name]}]
    )

    logger.debug("Response for describe_images: {}".format(response))

    images = response["Images"]
    if len(images) == 0:
        logger.warning("No image found for region {}".format(region))
        return None
    elif len(images) > 1:
        logger.warning(
            "{} images found for region {}. Only the first of the result is selected.".format(
                len(images), region
            )
        )

    return response["Images"][0]["ImageId"]


if __name__ == "__main__":
    main()
