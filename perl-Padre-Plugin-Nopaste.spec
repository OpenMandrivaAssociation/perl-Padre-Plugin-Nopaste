%define upstream_name    Padre-Plugin-Nopaste
%define upstream_version v0.3.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Send code on a nopaste website from padre
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Nopaste)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Padre)
BuildRequires: perl(Padre::Plugin)
BuildRequires: perl(Padre::Task)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(parent)

%description
This plugin allows one to send stuff from Padre to a nopaste website with
Ctrl+Shift+V, allowing for easy code / whatever sharing without having to
open a browser.

It is using 'App::Nopaste' underneath, so check this module's pod for more
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

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
