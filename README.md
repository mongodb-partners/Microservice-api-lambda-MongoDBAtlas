### Project Overview

This is a Serverless Application Model (SAM) project for a Python MongoDB CRUD microservice. The project utilizes AWS Lambda as serverless functions and API Gateway for interaction. With this project, you have the flexibility to either use an existing MongoDB cluster connection string or provision a new cluster directly through the application.

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

Before deploying the application, you must prepare your MongoDB. There are two options available:

#### Use Existing Connection String

- Ensure you have the complete MongoDB srv connection string with your username & password included.
- Ensure that Lambda can access your cluster. For testing purposes, you can use `0.0.0.0/0` in your network IP access list.
- In production, consider setting up a VPC peering connection between your AWS cloud VPC and the Atlas VPC. This will restrict public access and only accept connections from your VPC. Learn more about VPC peering in the [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/security-vpc-peering/).

#### Provisioning a New ATLAS Cluster

For automating the environment setup needed to deploy an Atlas cluster from the application, we will use ATLAS AWS CDK.

**Pre-requisite:**

1. Install AWS CDK:
    ```bash
    sudo npm install -g aws-cdk
    ```

2. Navigate to the `/atlas-aws-bootstrap-cdk` folder in this repository. 

**CDK & Project Setup:**

1. Bootstrap your AWS account:
    ```bash
    cdk bootstrap aws://ACCOUNT_NUMBER/REGION
    ```

2. Deploy the project you pulled from prerequisites:
    ```bash
    npx cdk diff 
    npx cdk deploy 
    ```

    This should deploy all the necessary resources and set up the environment in your AWS account so that we can deploy a new Atlas cluster in your Atlas account.

**Next:**

3. Obtain your Organization ID from MongoDB Atlas:

    - To retrieve your Organization ID, navigate to the organization page within MongoDB Atlas.
    - Go to "Settings" where you'll find your Organization ID displayed. You can also copy the Organization ID from this section for ease of use.

4. Adding MongoDB Organization Public & Private Key to AWS Secrets Manager:

    - To obtain your MongoDB organization API Key, log in to your Atlas account and follow the instructions provided in the official documentation [MongoDB Organization Access](https://www.mongodb.com/docs/atlas/configure-api-access-org/).
    - To securely store your MongoDB organization's Public and Private API Keys, navigate to AWS Secrets Manager and go to this secret - `cfn/atlas/profile/default`. Update the public key and private key in the secrets.

    **Note:** Alternatively, if you don't want to use the CDK or want to do it manually, you can follow this guide [link](https://www.mongodb.com/developer/products/atlas/deploy-mongodb-atlas-aws-cdk-typescript/).

---

#### SAM Commands

1. Move back to the root directory of the project.

2. Execute the following command:

    ```bash
    sam deploy --guided
    ```
    
Follow the guided deploy instructions:

- Set `ProvisionNewCluster` to true if provisioning a new cluster, and provide the required parameters.
- If `ProvisionNewCluster` is false, skip all the Atlas parameters and specify `ConnectionString` and `CollectionName`.

Follow the instructions and wait for the CloudFormation stack to finish creating the stack.

---

### Verification and Validation

After deployment, you will receive the API gateway link in the outputs. Use this link in Postman or any request maker. Check out the Postman collection below to test out the APIs. Also, after forking, update the API Gateway URL in variables with your API Gateway URL from the outputs:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/21766500-90eb1521-2e04-41bf-bce4-bf147bf667e1?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D21766500-90eb1521-2e04-41bf-bce4-bf147bf667e1%26entityType%3Dcollection%26workspaceId%3Db95c81f7-c54b-471f-a9b1-ae8d56518746)

Alternatively, you can import the Postman collection 'postman/Python-Microservice.postman_collection.json' into your Postman to test the API.


### How to Publish?

To publish your application, you can utilize the AWS Serverless Application Model (SAM) through the terminal. By default, your application will be published as a Private App. After publication, you have the option to convert it to a Public App.

For detailed guidance on publishing applications using SAM, refer to the [SAM Publish Application documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html).