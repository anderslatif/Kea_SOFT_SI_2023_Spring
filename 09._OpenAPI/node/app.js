import express from "express";
const app = express();

app.use(express.json());

import swaggerUi from "swagger-ui-express";

const swaggerDefinition = {
    openapi: "3.0.0",
    info: {
        title: "OpenAPI Examnple API",
        version: "1.0.0",
        description: "A simple Express API that utilizes OpenAPI",
    },
};
const options = {
    swaggerDefinition,
    apis: ["./routers/*.js"],
};
app.use("/docs", swaggerUi.serve, swaggerUi.setup(options));

import usersRouter from "./routers/usersRouter.js";
app.use(usersRouter);


app.listen(8080, () => console.log("Server is running on port", 8080));
