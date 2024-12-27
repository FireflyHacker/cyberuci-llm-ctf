---
title: "Cyber@UCI Large Language Models Capture-the-Flag"
date: 2023-11-09T14:46:08+01:00
draft: true
---


The aim of the competition is to find out whether simple prompting and filtering mechanisms can make LLM applications robust to prompt injection and extraction.

## Competition Overview

In this competition, participants assume the roles of defenders and attackers:

- **Defenders** will craft prompts and filters to instruct an LLM to keep a secret, aiming to prevent its discovery in a conversation.
- **Attackers** will design strategies to extract the secret from the LLM, circumventing the defender's safeguards.

This mirrors the real-world security convention, in which defenders must anticipate and prepare for attacks, while attacks can adapt to the defenses in place.


## Prizes and Incentives

- **Prize Pool**: The top 3 defense teams and top 3 attack teams will receive cash prizes of **$000**, **$00**, and **$0**, for a total of **$0**.
- **Presentation**: Winners will be forced to tell Cyber@UCI board members how they did it.
- **Recognition**: Chance for you to be regcognised by famous hackers such as: Kamaii, Caraboo, and Fireflyhacker

## Important Links

- [Official Rules](/static/rules.pdf)
- [API Documentation](/docs)
- [API Key](/api-key)
- [Defense Testing Interface](/defense)
- [Attack Testing Interface](/attack)


## Why This Competition?

Current large language models (LLMs) cannot yet follow initial instructions reliably, 
if adversarial users or third parties can later provide input to the model.
This is a major obstacle to using LLMs as the core of a user-facing application.
There exists a growing toolbox of [attacks](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/)
that make LLMs obey the attacker's instructions, and defenses of varying complexity to counter them.

Application developers who *use* LLMs, however, can't always be expected to apply complex defense mechanisms.
We aim to find whether a simple approach exists that can withstand adaptive attacks.

## Rules and Engagement

For the complete set of rules, please visit the [official rules page](/static/rules.pdf).
Collaboration between teams, including between distinct teams in the Attack and Defense track, is not allowed.

**By using this chat interface and the API, you accept that the interactions with the interface and the API can be used
for research purposes, and potentially open-sourced by the competition organizers.**

### Why this setup?

The goal of the competition is to find out whether there exists a simple *prompting* approach on the models tested
that can make them robust, or robust enough that simple *filtering* approaches can patch up the remaining vulnerabilities.

We see this fundamentally as a *security* problem: thus the defenders cannot change or adapt their defenses once the Reconnaissance phase begins.

We depart from the standard security threat model in two ways:

- The defender is allowed prompting, LLM post-processing, and arbitrary post-processing in Python.

- We test whether attackers can break a defense in a query-limited setting once they are ready to attack any given defense.
The attack is scored based on the number of interactions and tokens it takes them to break the defense.

Both of these are reasonable tradeoffs to make it easier for participants to find interesting defenses and attacks,
and for the organizers to evaluate them.

We choose a black-box setting similar to the real-world LLM application threat model:
the attacker has no white-box access to the defender's security mechanism. 
However, they can do a large number of queries during the Reconnaissance phase to find out how any defense behaves.

## Models for Testing

The competition will use llama3 for testing.

## Testing and Credits

Teams can begin testing defenses immediately using the [Defense Interface](/defense).
There is a (large) upper limit on the number of API calls per day to prevent abuse and server overload.

Please note that the interface may be buggy on Safari (the CSS may not load properly).
Please use another browser, or reload the page until CSS is correctly loaded.


