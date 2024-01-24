export const handler = (event, context, callback) => {
  console.log("In nodejs Lambda function");
  console.log("TEST_VAR", process.env.TEST_VAR);

  // Returns a string
  // return callback(null, "Hello from Lambda");

  var response = {
    headers: { "Content-Type": "application/json" },
    statusCode: 200,
    body: JSON.stringify({ success: true, TEST_VAR: process.env.TEST_VAR }),
  };
  return callback(null, response);
};
