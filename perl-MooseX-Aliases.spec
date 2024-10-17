%define upstream_name    MooseX-Aliases
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Attribute metaclass trait for L<MooseX::Aliases>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-Aliases-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 662125
- update to new version 0.10

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2
+ Revision: 657340
- rebuild for updated spec-helper

* Sun Feb 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 637634
- update to new version 0.09

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 492953
- update to 0.08

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 473721
- update to 0.07

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 470662
- adding missing buildrequires:
- import perl-MooseX-Aliases


* Fri Nov 27 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

