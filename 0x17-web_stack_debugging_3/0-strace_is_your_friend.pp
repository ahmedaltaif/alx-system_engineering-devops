#Apache is returning a 500 error
exec { 'sed':
  command => 'sed -i "s|.phpp|.php|" /var/www/html/wp-settings.php',
  path    => '/bin/'
}
