[ loadI 8 => r3; loadI 12 => r4 ]
[ load r3 => r2; add r3, r4 => r1 ]
[ load r1 => r0; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ store r0 => r1; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ nop ; nop  ]
[ output 12; nop  ]