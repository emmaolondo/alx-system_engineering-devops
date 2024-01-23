# a file that specifies the owner, group, mode  and content using puppet
file {'/tmp/school':
  ensure  => present,
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
