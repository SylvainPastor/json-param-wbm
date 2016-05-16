# Makefile for JSON paramter webmin module

FILES = \
	CHANGES \
	lang/en \
	config \
	config.info \
	edit.cgi \
	index.cgi \
	install_check.pl \
	log_parser.pl \
	module.info \
	save.cgi \
	json-param-lib.pl \
	VERSION

all:

dist: json-param-wbm.tgz

localdist: local-wbm.tgz

optdist: opt-wbm.tgz

clean:
	-rm -f json-param-wbm.tgz local-wbm.tgz opt-wbm.tgz
	-rm -rf json-param-wbm

json-param-wbm.tgz: $(FILES)
	@echo 'Creating JSON paramter Webmin Module archive in "json-param-wbm.tgz" ...'
	@-rm -rf json-param-wbm json-param-wbm.tgz
	@mkdir json-param-wbm
	@tar cf - $(FILES) | tar xf - -C json-param-wbm
	@tar cf - json-param-wbm | gzip > json-param-wbm.tgz
	@rm -rf json-param-wbm
	@echo Done.

local-wbm.tgz: $(FILES)
	@echo 'Creating JSON paramter Webmin Module archive in "local-wbm.tgz" ...'
	@-rm -rf json-param-wbm local-wbm.tgz
	@mkdir json-param-wbm
	@tar cf - $(FILES) | tar xf - -C json-param-wbm
	@cp config-usr-local-json-param json-param-wbm/config
	@tar cf - json-param-wbm | gzip > local-wbm.tgz
	@rm -rf json-param-wbm
	@echo Done.

opt-wbm.tgz: $(FILES)
	@echo 'Creating JSON paramter Webmin Module archive in "opt-wbm.tgz" ...'
	@-rm -rf json-param-wbm opt-wbm.tgz
	@mkdir json-param-wbm
	@tar cf - $(FILES) | tar xf - -C json-param-wbm
	@cp config-opt-json-param json-param-wbm/config
	@tar cf - json-param-wbm | gzip > opt-wbm.tgz
	@rm -rf json-param-wbm
	@echo Done.
