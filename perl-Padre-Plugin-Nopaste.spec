%define upstream_name    Padre-Plugin-Nopaste
%define upstream_version v0.3.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Send code on a nopaste website from padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::Nopaste)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Util)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Padre::Plugin)
BuildRequires:	perl(Padre::Task)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)

BuildArch:	noarch

Requires:	perl(parent)

%description
This plugin allows one to send stuff from Padre to a nopaste website with
Ctrl+Shift+V, allowing for easy code / whatever sharing without having to
open a browser.

It is using 'App::Nopaste' underneath, so check this module's pod for more
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 656953
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 597196
- update to v0.3.1

* Sat Aug 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 569764
- skip test, requiring a display
- update to v0.3.0

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.1-2mdv2010.0
+ Revision: 375916
- rebuild

* Sun Apr 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 364103
- adding missing prereq
- import perl-Padre-Plugin-Nopaste


* Sun Apr 05 2009 cpan2dist 0.2.0-1mdv
- initial mdv release, generated with cpan2dist

