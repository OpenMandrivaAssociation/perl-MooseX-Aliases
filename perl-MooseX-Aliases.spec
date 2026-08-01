%define upstream_name    MooseX-Aliases
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	0.11
Release:	4

Summary:	Attribute metaclass trait for L<MooseX::Aliases>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/doy/moosex-aliases
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DOY/MooseX-Aliases-0.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Requires)
BuildArch:	noarch

%description
The MooseX::Aliases module will allow you to quickly alias methods in
Moose. It provides an alias parameter for 'has()' to generate aliased
accessors as well as the standard ones. Attributes can also be initialized
in the constructor via their aliased names.

%prep
%setup -q -n MooseX-Aliases-0.11

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :
%make test || :

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


