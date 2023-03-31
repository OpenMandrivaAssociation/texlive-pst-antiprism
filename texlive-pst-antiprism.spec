Name:		texlive-pst-antiprism
Version:	46643
Release:	2
Summary:	A PSTricks related package which draws an antiprism
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-antiprism
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-antiprism.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-antiprism.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-antiprism is a PSTricks related package which draws an
antiprism, which is a semiregular polyhedron constructed with
2-gons and triangles.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-antiprism
%{_texmfdistdir}/tex/generic/pst-antiprism
%{_texmfdistdir}/dvips/pst-antiprism
%doc %{_texmfdistdir}/doc/generic/pst-antiprism

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
