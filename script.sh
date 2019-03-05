#!/bin/bash
# Sends the output of a python script to a slack message
export APP_SLACK_WEBHOOK='https://hooks.slack.com/services/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'


slack-message "#mfleitas" `$@`
