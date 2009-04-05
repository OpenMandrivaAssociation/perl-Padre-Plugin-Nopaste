
%define realname   Padre-Plugin-Nopaste
%define version    0.2.1
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Send code on a nopaste website from padre
Source:     http://www.cpan.org/modules/by-module/Padre/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(App::Nopaste)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Padre)
BuildRequires: perl(Padre::Plugin)
BuildRequires: perl(Padre::Task)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(parent)
Requires: perl(parent)

BuildArch: noarch

%description
This plugin allows one to send stuff from Padre to a nopaste website with
Ctrl+Shift+V, allowing for easy code / whatever sharing without having to
open a browser.

It is using 'App::Nopaste' underneath, so check this module's pod for more
information.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


