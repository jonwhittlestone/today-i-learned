//import { SQS } from '@aws-sdk/client-sqs';
//import { fromEnv } from "@aws-sdk/credential-providers";

// import winstonpkg from 'winston';
// const { transports, Logger } = winstonpkg;


// var logger = new Logger({
//     level: 'info',
//     transports: [transports.default()]
// });


// var sqs = new SQS({
//     credentials: fromEnv(),
//     region: process.env.AWS_REGION
// });

const queueUrl = process.env.QUEUE_URL;

export function handler(event, context, callback) {
    // logger.info('START processing');
    console.log('in script');

    // var params = {
    //     MessageBody: event.body,
    //     QueueUrl: queueUrl
    // };

    // sqs.sendMessage(params, function(err, data){
    //     if (err) {
    //         logger.error('There was a problem enqueue-ing: ' + err.message);
    //         var err_response = {
    //             headers: {'Content-Type': 'application/json'},
    //             statusCode: 500,
    //             body: JSON.stringify({success: false, errorMsg: err.message})
    //         }
    //         callback(err, null);
    //     } else {
    //         var response = {
    //             headers: {'Content-Type': 'application/json'},
    //             statusCode: 200,
    //             body: JSON.stringify({success: true})
    //         };
    //         logger.info('Successfully enqueued');
    //         callback(null, response);
    //     }
    // });

    // logger.info('END processing');

}

if (!process.env.AWS_EXECUTION_ENV) {
  handler();
}