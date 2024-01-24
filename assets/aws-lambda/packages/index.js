import { SQS } from "@aws-sdk/client-sqs";
import { fromEnv } from "@aws-sdk/credential-providers";

import winstonpkg from "winston";
const { Logger, transports } = winstonpkg;

export const handler = (event, context, callback) => {
  console.log("In nodejs packages Lambda function: 11:32");
  var response = {
    headers: { "Content-Type": "application/json" },
    statusCode: 200,
    body: JSON.stringify({ success: true }),
  };
  return callback(null, response);
};
