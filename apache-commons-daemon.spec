%define short_name commons-daemon
%define java_path %(dirname $(dirname $(readlink -f $(which javac))))
Name:           apache-%{short_name}
Version:        1.3.4
Release:        3%{?dist}
Summary:        Commons Daemon - Controlling of Java Daemons
URL:            https://commons.apache.org/daemon/
License:        Apache-2.0
Source0:        https://dlcdn.apache.org//commons/daemon/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  libcap-devel
BuildRequires:  gcc
BuildRequires:  java-11-openjdk-devel
Requires(pre):  shadow-utils
Requires:       java-11-openjdk
Requires:       java-11-openjdk-headless

%description
The Daemon Component contains a set of Java and native code, including
a set of Java interfaces applications must implement and Unix native
code to control a Java daemon from a Unix operating system.

%package        jsvc
Summary:        Java daemon launcher
Group:          System/Daemons
Provides:       jsvc = %{version}-%{release}
Obsoletes:      jsvc < %{version}

%description    jsvc
Jsvc is a set of libraries and applications for making Java applications run on
UNIX more easily. It allows the application (e.g. Tomcat) to perform some
privileged operations as root (e.g. bind to a port < 1024), and then switch
identity to a non-privileged user.


%prep

# The macro setup is used to unpack sources
%setup -q -n %{short_name}-%{version}-src


%build
cd src/native/unix
%configure --with-java=%{java_path}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}/

install -m 775 src/native/unix/jsvc $RPM_BUILD_ROOT%{_bindir}/jsvc


%pre
exit 0

%post

%preun

%postun

%files jsvc
%license LICENSE.txt
%{_bindir}/jsvc

%changelog
* Fri Oct 27 2023 Armando Basile <info@tasolutionsrls.it> 1.3.4-3
- release 1.3.4


