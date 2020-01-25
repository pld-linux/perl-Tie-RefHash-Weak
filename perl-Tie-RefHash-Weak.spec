#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Tie
%define		pnam	RefHash-Weak
Summary:	Tie::RefHash::Weak - A Tie::RefHash subclass with weakened references in the keys
Name:		perl-Tie-RefHash-Weak
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7c6793fab417c9761d88f596dfb32e9
URL:		http://search.cpan.org/dist/Tie-RefHash-Weak/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Variable-Magic
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::RefHash module can be used to access hashes by reference.
This is useful when you index by object, for example.

The problem with Tie::RefHash, and cross indexing, is that sometimes
the index should not contain strong references to the objecs.
Tie::RefHash's internal structures contain strong references to the
key, and provide no convenient means to make those references weak.

This subclass of Tie::RefHash has weak keys, instead of strong ones.
The values are left unaltered, and you'll have to make sure there are
no strong references there yourself.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Tie/RefHash/Weak.pm
%{_mandir}/man3/Tie::RefHash::Weak.3pm*
