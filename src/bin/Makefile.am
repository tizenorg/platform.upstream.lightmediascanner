MAINTAINERCLEANFILES = Makefile.in

AM_CPPFLAGS = \
	-I$(top_srcdir)/src/lib \
	@SQLITE3_CFLAGS@

lms_PROGRAMS = \
	lms-test \
	lms-list-parsers


lms_test_SOURCES = test.c
lms_test_LDADD = $(top_builddir)/src/lib/liblightmediascanner.la @SQLITE3_LIBS@
lms_test_DEPENDENCIES = $(top_builddir)/src/lib/liblightmediascanner.la


lms_list_parsers_SOURCES = list-parsers.c
lms_list_parsers_LDADD = $(top_builddir)/src/lib/liblightmediascanner.la \
	@SQLITE3_LIBS@
lms_list_parsers_DEPENDENCIES = $(top_builddir)/src/lib/liblightmediascanner.la
