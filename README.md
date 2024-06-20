### Project Overview

This is a Serverless Application Model (SAM) project for a Python MongoDB CRUD microservice. The project utilizes AWS Lambda as serverless functions and API Gateway for interaction. With this project, you have the flexibility to use an existing MongoDB cluster connection string.

The primary functionalities of the project include Create, Read, Update, and Delete operations on MongoDB data. By leveraging AWS Lambda and API Gateway, this project offers a scalable and cost-effective solution for deploying serverless applications with MongoDB integration.

---

### Prerequisites

Before proceeding, ensure you have the following prerequisites installed:

- [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Create IAM User for AWS CLI, Create Access Keys & secret keys
- Configure AWS CLI using `aws configure` with Account Id, Access Key, Secret Key, and Region
- [Install SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Install Docker](https://docs.docker.com/engine/install/)
- This application requires a minimum version of Python 3.10 to run. You can install Python 3.10 from [Install Python](https://www.python.org/downloads/)

---

### Build Stage

To build the project locally, execute the following command:

```bash
sam build
```

This command will locally build the project, and output files will be saved in the `.aws-sam` folder.

---

### Deploy Stage

Before deploying the application, you must prepare your MongoDB.

#### Use Existing Connection String

- Ensure you have the complete MongoDB srv connection string with your username & password included.
- Ensure that Lambda can access your cluster. For testing purposes, you can use `0.0.0.0/0` in your network IP access list.
- In production, consider setting up a VPC peering connection between your AWS cloud VPC and the Atlas VPC. This will restrict public access and only accept connections from your VPC. Learn more about VPC peering in the [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/security-vpc-peering/).


#### SAM Commands

1. Execute the following command:

    ```bash
    sam deploy --guided
    ```
    
Follow the guided deploy instructions:

-  Specify `ConnectionString` , `DBName` and `CollectionName`.

Follow the instructions and wait for the CloudFormation stack to finish creating the stack.

---

### Verification and Validation

After deployment, you will receive the API gateway link in the outputs. Use this link in Postman or any request maker. Check out the Postman collection below to test out the APIs. Also, after forking, update the API Gateway URL in variables with your API Gateway URL from the outputs:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/21766500-90eb1521-2e04-41bf-bce4-bf147bf667e1?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D21766500-90eb1521-2e04-41bf-bce4-bf147bf667e1%26entityType%3Dcollection%26workspaceId%3Db95c81f7-c54b-471f-a9b1-ae8d56518746)

Alternatively, you can import the Postman collection 'postman/Python-Microservice.postman_collection.json' into your Postman to test the API.


### How to Publish?

To publish your application, you can utilize the AWS Serverless Application Model (SAM) through the terminal. By default, your application will be published as a Private App. After publication, you have the option to convert it to a Public App.

For detailed guidance on publishing applications using SAM, refer to the [SAM Publish Application documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html).