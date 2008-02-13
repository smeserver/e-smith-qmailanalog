#
# RPM spec file for e-smith CGI interface to qmailanalog reports
#
Summary: e-smith module for analysing qmail logs
%define name e-smith-qmailanalog
Name: %{name}
%define version 1.12.0
%define release 3
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-qmailanalog-1.12.0-tags2general.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base, qmailanalog >= 0.70-03, daemontools >= 0.70, tai64nunix
Requires: e-smith-lib >= 1.13.1-08
Requires: e-smith-formmagick >= 1.4.0-9
BuildRequires: e-smith-devtools
AutoReqProv: no

%changelog
* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.12.0-3
- Remove <base> tags now in general [SME: 3921]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.2-02
- Bump release number only

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-03]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-02]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- Spanish nav bar [gordonr 9153]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-07]
- Add Spanish lexicon for qmailanalog [lijied 3793]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-06]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-05]
- Modified qmailanalog panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-04]
- Split en-us lexicon from qmailanalog panel [lijied 4030]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-03]
- Added French lexicon for qmailanalog. [lijied 5003]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-02]
- Use the new gen_locale_date_string routine [markk 3357]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-01]
- Forced version update by co2rpm to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to maintained stream number to 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.4-01]
- Set up PATH variable so that qmailanalog can find things like tr and awk.
  [charlieb 3598]
- Redirect STDERR from cat so that errors due to there being no @* files yet
  do not appear in the admin error log. [charlieb 3598]

* Fri May  3 2002 Mark Knox <markk@e-smith.com>
- [1.5.3-01]
- Display the date in a localised way [markk 3321]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.2-01]
- Language en->en-us

* Thu Apr 11 2002 Mark Knox <markk@e-smith.com>
- [1.5.1-01]
- Moved all code into module qmailanalog.pm. [markk 3156]
- Converted to FormMagick panel and internationalized [markk 3156]
- added POD and testsuite [markk 3156]

* Thu Apr 11 2002 Mark Knox <markk@e-smith.com>
- [1.5.0-01]
- new development stream from cvs sources

* Thu Apr 11 2002 Mark Knox <markk@e-smith.com>
- [1.4.1-01]
- rollRPM: Rolled version number to 1.4.1-01. Includes patches up to 1.4.0-06.

* Fri Aug 17 2001 gordonr
- [1.4.0-06]
- Autorebuild by rebuildRPM

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-05]
- Minor grammatical changes

* Tue May 1 2001 Peter Samuel <peters@e-smith.com>
- [1.4.0-04]
- Now handles multilog files instead of older cyclog files
- Adds qmail-qstat and qmail-qread to reports

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.4.0-03]
- Rolling release number for GPG signing.

* Mon Jan 29 2001 Peter Samuel <peters@e-smith.com>
- [1.4.0-02]
- Report output now cooks special HTML characters.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-03.

* Mon Jan 15 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-03]
- Changes to the ordering of the e-smith manager 

* Fri Jan 05 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-2]
- Updated copyright information and removed warning
  messages sent to logs for lack of prototypes in
  qmail-analog panel

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [1.3.0-1]
- Rolled version to 1.3.0-1. Includes patches up to 1.1-3

* Tue Nov 07 2000 Adrian Chung <adrianc@e-smith.com>
- Changed panel to be in "Miscellaneous" section.

* Tue Oct 31 2000 Charlie Brady <charlieb@e-smith.com>
- Remove references to obsolete services database.

* Thu Oct 26 2000 Peter Samuel <peters@e-smith.com>
- Rolled version to 1.1. Includes patches up to 1.0-4

* Tue Oct 24 2000 Adrian Chung <adrian.chung@e-smith.com>
- Instead of using a table rows, just wrap output in PRE's.

* Thu Oct 20 2000 Adrian Chung <adrian.chung@e-smith.com>
- HTMLized the output of qmailanalog reports.
- Changed spec file to use genfilelist.

* Thu Oct 19 2000 Adrian Chung <adrian.chung@e-smith.com>
- Updated scripts in web/functions directory to pass
  merged configuration and services db hash.

* Wed Aug 16 2000 Peter Samuel <peters@e-smith.com>
- initial release

%description
e-smith cgi interface to qmailanalog.

qmailanalog provides a number of programs to help analyse qmail logs.
This program uses the e-smith manager to allow the administrator to
choose a report.

%prep
%setup
%patch0 -p1

%build
mkdir -p root/etc/e-smith/web/panels/manager/cgi-bin
perl createlinks
/sbin/e-smith/buildtests 30e-smith-qmailanalog

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
