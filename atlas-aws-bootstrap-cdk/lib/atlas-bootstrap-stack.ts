import * as cdk from 'aws-cdk-lib'
import { Construct } from 'constructs'
import {
  MongoAtlasBootstrap,
  MongoAtlasBootstrapProps,
  AtlasBasicResources
} from 'awscdk-resources-mongodbatlas'

export class AtlasBootstrapStack extends cdk.Stack {
  constructor (scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const roleName = 'MongoDB-Atlas-CDK-Excecution'
    const mongoDBProfile = 'default'   

    const bootstrapProperties: MongoAtlasBootstrapProps = {
      roleName,      secretProfile: mongoDBProfile,
      typesToActivate: ['ServerlessInstance', ...AtlasBasicResources]
    }

    new MongoAtlasBootstrap(this, 'mongodb-atlas-bootstrap', bootstrapProperties)
  }
}