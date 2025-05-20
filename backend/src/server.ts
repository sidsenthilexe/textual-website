import express from 'express';
import dotenv from 'dotenv';
import fetch from 'node-fetch';
dotenv.config();

const server = express();
const PORT = process.env.PORT || 3000;
const TS_API_KEY = process.env.TS_API_KEY;

server.get("/", (_req, res) => {
    res.send("Running :)")
});

server.get("/tailscale/devices", async (_req, res) => {
    if (!TS_API_KEY) {
        return res.status(500).send("API Key not set");
    }
    const response = await fetch("")
})

server.listen(PORT, () => {
    console.log(`running on port ${PORT}`)
});