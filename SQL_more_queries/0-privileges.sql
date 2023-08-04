#!/bin/bash

# MySQL user account to list privileges for
USERS=("user_0d_1" "user_0d_2")

# Loop through each user and list privileges
for user in "${USERS[@]}"; do
    echo "Privileges for user: $user"
    mysql --login-path=local -e "SHOW GRANTS FOR '$user'@'localhost';"
    echo "-------------------------------------"
done
