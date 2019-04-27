<?php

$arr = [
  [
    'name' => 'Taro',
    'age'  => 24
  ],
  [
    'name' => 'Goro',
    'age'  => 25
  ],
  [
    'name' => 'Jiro',
    'age'  => 32
  ]
];

$result = array_map(function($obj) { return $obj['age']; }, $arr);

print_r($result);
?>
