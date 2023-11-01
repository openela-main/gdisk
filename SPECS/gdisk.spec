Summary:       An fdisk-like partitioning tool for GPT disks
Name:          gdisk
Version:       1.0.3
Release:       11%{?dist}
License:       GPLv2
URL:           http://www.rodsbooks.com/gdisk/
Group:         System Environment/Base
Source0:       http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
Patch0:        gdisk-1.0.3-byteswap.patch
Patch1:        gdisk-CVE-2020-0256.patch
Patch2:        gdisk-CVE-2021-0308.patch
BuildRequires: popt-devel
BuildRequires: libuuid-devel
BuildRequires: ncurses-devel

%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%setup -q -n gptfdisk-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod 0644 gdisk_test.sh

%build
make CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" LDFLAGS="%{build_ldflags}"

%install
for f in gdisk sgdisk cgdisk fixparts ; do 
    install -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    install -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%files
%license COPYING
%doc NEWS README gdisk_test.sh
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/cgdisk.8*
%{_mandir}/man8/sgdisk.8*
%{_mandir}/man8/fixparts.8*

%changelog
* Tue Mar 15 2022 Nikola Forró <nforro@redhat.com> - 1.0.3-11
- Fix double byteswap on big-endian systems also while reading partition names
  resolves: #2065205

* Wed Mar 02 2022 Nikola Forró <nforro@redhat.com> - 1.0.3-10
- Fix CVE-2021-0308
  resolves: #2052364

* Wed Mar 02 2022 Nikola Forró <nforro@redhat.com> - 1.0.3-9
- Fix CVE-2020-0256
  resolves: #2052365

* Mon Oct 25 2021 Nikola Forró <nforro@redhat.com> - 1.0.3-8
- Add upstream tests as a gating test
  related: #1899990

* Wed Sep 29 2021 Nikola Forró <nforro@redhat.com> - 1.0.3-7
- Fix incorrect byte order of partition names on big-endian systems
  resolves: #1899990

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 1.0.3-6
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1.0.3-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Fri Jul 28 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-2
- Ship NEWS

* Fri Jul 28 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-1
- 1.0.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 21 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.8.10-2
- Drop icu from buildreq

* Sat Mar 08 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.8.10-1
- 0.8.10

* Sun Mar 02 2014 Terje Rosten <terje.rosten@ntnu.no> - 0.8.9-1
- 0.8.9

* Wed Feb 12 2014 Nils Philippsen <nils@redhat.com> - 0.8.8-2
- fix bogus dates in changelog
- rebuild for new libicu

* Thu Oct 17 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.8.8-1
- 0.8.8

* Fri Sep 13 2013 Richard W.M. Jones <rjones@redhat.com> - 0.8.7-2
- Range check -i option (RHBZ#1007847).

* Sun Aug 11 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.8.7-1
- 0.8.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.6-1
- Update to 0.8.6

* Sat Nov 17 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.5-1
- 0.8.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.4-1
- 0.8.4

* Sat Apr 21 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.8.2-3
- Rebuild for libicu 49.1.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for c++ ABI breakage

* Sun Jan 29 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.2-1
- 0.8.2

* Thu Jan 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-3
- Add patch to build with gcc 4.7

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-2
- Add cgdisk and fixparts

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1
- 0.8.1
- Add ncurses-devel to buildreq

* Thu Sep 08 2011 Orion Poplawski <orion@cora.nwra.com> - 0.7.2-2
- Rebuild for libicu 4.8.1

* Sun Jul 10 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.7.2-1
- 0.7.2

* Mon Apr 11 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.7.1-1
- 0.7.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.6.14-1
- 0.6.14

* Thu Nov 11 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.13-1
- 0.6.13

* Fri Jun 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.8-1
- 0.6.8

* Thu Mar 25 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-1
- 0.6.6
- Compile with -D_FILE_OFFSET_BITS=64, recommended upstream

* Sat Mar 20 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.5-1
- 0.6.5
- Add alignment patch (bz #575297)

* Thu Mar 11 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-2
- Fix source url

* Sun Feb 14 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-1
- 0.6.3

* Sun Jan 31 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.2-1
- 0.6.2

* Mon Jan 25 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.1-1
- 0.6.1
- add popt-devel to buildreq
- random clean up

* Fri Jan 15 2010 R Smith <rodsmith@rodsbooks.com> - 0.6.0
- created spec file for 0.6.0 release
