 Puppet script to edit typo on php file

$file_path = '/var/www/html/wp-settings.php'

# edit "phpp" to "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}