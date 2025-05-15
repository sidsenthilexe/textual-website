import express from 'express';
import dotenv from 'dotenv';
import fetch from 'node-fetch';
dotenv.config();

const server = express();
const PORT = process.env.PORT || 3000;

server.get("/", (_req, res) => {
    res.send("Running :)")
});

server.listen(PORT, () => {
    console.log(`running on port ${PORT}`)
});