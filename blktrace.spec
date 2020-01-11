Summary: Utilities for performing block layer IO tracing in the linux kernel
Name: blktrace
Version: 1.0.5
Release: 8%{?dist}
License: GPLv2+
Group: Development/System
Source:  http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
Url: http://brick.kernel.dk/snaps

Requires: python
BuildRequires: libaio-devel python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0: blktrace-1.0.5-blktrace-high-cpu-count.patch
Patch1: blktrace-1.0.5-remove-k-from-manpage.patch
Patch2: blktrace-1.0.5-signal-condition.patch

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space.  This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make CFLAGS="%{optflags}" all

%install
rm -rf %{buildroot}
make dest=%{buildroot} prefix=%{buildroot}/%{_prefix} mandir=%{buildroot}/usr/share/man install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%attr(0644,root,root) /usr/share/man/man1/*
%attr(0644,root,root) /usr/share/man/man8/*

%changelog
* Wed May 18 2016 Eric Sandeen <sandeen@redhat.com> - 1.0.5-8
- One more cpu scalability fix (#1032368)

* Wed May 18 2016 Eric Sandeen <sandeen@redhat.com> - 1.0.5-7
- Add upstream cpu scalability patches (#1032368)
- Remove "-k" option from manpage (#1300354)
- Fix potential deadlock when calling stop_tracers (#1263189)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.0.5-6
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.5-5
- Mass rebuild 2013-12-27

* Thu Mar 21 2013 Eric Sandeen <sandeen@redhat.com> - 1.0.5-4
- Remove tex->pdf doc build, fix build & lighten up buildreqs

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Eric Sandeen <sandeen@redhat.com> - 1.0.5-1
- New upstream version

* Tue Jan 31 2012 Eric Sandeen <sandeen@redhat.com> - 1.0.4-1
- New upstream version

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.3-1
- New upstream version

* Wed Mar 16 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.2-1
- New upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Eric Sandeen <sandeen@redhat.com> - 1.0.1-4
- Fix linking with libpthread (#564775)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-2
- Upstream respun the release tarball to re-include top-level dir
- drop exclude of bno_plot.py[co], not getting built now?

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-1
- New upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.0-2
- Build PDF documentation after all

* Sun Nov 02 2008 Eric Sandeen <sandeen@redhat.com> - 1.0.0-1
- New upstream version (now with actual versioning!)

* Fri Feb 08 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.9.20080103162505git
- gcc-4.3 rebuild

* Sat Jan 26 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.8.20080103162505git
- New upstream version

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.6.20071010202719git
- Add libaio-devel to BuildRequires

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.5.20071010202719git
- New upstream version

* Wed Aug 15 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.4.20070730162628git
- Fix up btt/Makefile to accept rpm's CFLAGS

* Tue Aug 14 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.3.20070730162628git
- Just drop the pdf build, bloats the buildroot for such a simple tool

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.2.20070730162628git
- Add ghostscript to BuildRequires, use attr macro for man pages

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.1.20070730162628git
- New package, initial build.
