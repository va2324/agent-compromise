FROM node:22 AS node

FROM python:3.13

COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm && ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

RUN python --version && node --version && npm --version && npx --version

WORKDIR /agent

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./agent.py" ]