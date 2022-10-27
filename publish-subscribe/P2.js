#!/usr/bin/env node

var amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var msg = [{
            productor: 'P2',
            en: 'Beta',
            timestamp: Date.now(),
         }];

        var queue = 'b';

        channel.assertQueue(queue, {
            durable: false
        });
        channel.sendToQueue(queue, Buffer.from(JSON.stringify(msg)));

        console.log(" [x] Sent %r", msg);
    });
    setTimeout(function() {
        connection.close();
        process.exit(0);
    }, 500);
});