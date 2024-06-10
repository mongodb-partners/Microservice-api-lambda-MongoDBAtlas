#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AtlasBootstrapStack } from '../lib/atlas-bootstrap-stack';

const app = new cdk.App();
const env = { region: process.env.CDK_DEFAULT_REGION, account: process.env.CDK_DEFAULT_ACCOUNT };

new AtlasBootstrapStack(app, 'AtlasBootstrapStack', { env });