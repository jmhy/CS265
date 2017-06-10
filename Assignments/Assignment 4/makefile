db = sample.db
tmp = sample.db.tmp

.PHONY : build
build : cddb
	-@echo "Written in Python, so just giving exec permission to cddb"
	chmod +x $<
clean :
	-@echo "In case the tmp db wasn't removed when overwriting old db"
	- \rm sample.db.tmp
view :
	less cddb
