# TODO:
# - warning: Installed (but unpackaged) file(s) found:
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel.rb
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel/mustache_extension.rb
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel/view.mustache
# - rm -r ri/Rack? (see XXX below)

%define pkgname mustache
Summary:	Logic-less templates.
Name:		ruby-mustache
Version:	0.11.2
Release:	0.1
License:	MIT
Source0:	http://github.com/defunkt/mustache/tarball/v0.11.2/%{name}-%{version}.tar.gz
# Source0-md5:	fc6e868cf09d40eaf36ffabaf1f412c4
Group:		Libraries
URL:		http://mustache.github.com/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to render
logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -c
mv defunkt-mustache-*/* .
rm -rf defunkt-mustache-*

%build

cp /usr/share/setup.rb .

rdoc --ri --op ri lib
rdoc --op rdoc lib
# XXX rm -r ri/Rack?
# rm -r ri/NOT_THIS_MODULE_RELATED_DIRS
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS HISTORY.md README.md
%{ruby_rubylibdir}/%{pkgname}.rb
%{ruby_rubylibdir}/%{pkgname}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mustache
%{ruby_ridir}/Rack
