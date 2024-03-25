# A resource declaration
file {'/tmp/school':
  Densure  => file,
  path    => '/tmp/school'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
