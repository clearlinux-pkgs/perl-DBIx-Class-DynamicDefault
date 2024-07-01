#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-Class-DynamicDefault
Version  : 0.04
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/DBIx-Class-DynamicDefault-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/DBIx-Class-DynamicDefault-0.04.tar.gz
Summary  : 'Automatically set and update fields'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-DBIx-Class-DynamicDefault-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBICx::TestDatabase)
BuildRequires : perl(DBIx::Class)
BuildRequires : perl(Module::Install)

%description
No detailed description available

%package dev
Summary: dev components for the perl-DBIx-Class-DynamicDefault package.
Group: Development
Provides: perl-DBIx-Class-DynamicDefault-devel = %{version}-%{release}
Requires: perl-DBIx-Class-DynamicDefault = %{version}-%{release}

%description dev
dev components for the perl-DBIx-Class-DynamicDefault package.


%package perl
Summary: perl components for the perl-DBIx-Class-DynamicDefault package.
Group: Default
Requires: perl-DBIx-Class-DynamicDefault = %{version}-%{release}

%description perl
perl components for the perl-DBIx-Class-DynamicDefault package.


%prep
%setup -q -n DBIx-Class-DynamicDefault-0.04
cd %{_builddir}/DBIx-Class-DynamicDefault-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Class::DynamicDefault.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
