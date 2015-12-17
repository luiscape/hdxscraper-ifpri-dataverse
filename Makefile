setup:
	bash bin/setup.sh;

test:
	bash bin/test.sh;

collect:
	bash bin/collect.sh;

register:
	bash bin/register.sh;

run:
	bash bin/collect.sh;
	bash bin/register.sh;
