import readline from 'readline-sync'
import chalk from 'chalk';
import color from 'colors';
import moment from 'moment';
import {IgApiClient,IgLoginTwoFactorRequiredError,IgCheckpointError,IgLoginRequiredError,IgUserHasLoggedOutError} from 'instagram-private-api'
import {existsSync, readFileSync, unlinkSync, writeFileSync, mkdirSync} from 'fs'
import Bluebird from 'bluebird';
import { PassThrough } from 'stream';
import inquirer from 'inquirer';

(async()=>{
    
    const username=readline.question("Enter your instagram username: ".blue);
    const password=readline.question("Enter your instagram password: ".blue);
    const ig = new IgApiClient()
   
    ig.state.generateDevice(username);
    writeFileSync('config.env', `user_name=${username}\npassword=${password}`);
 

  

  

        // Initiate Instagram API client
        // Perform usual login
        // If 2FA is enabled, IgLoginTwoFactorRequiredError will be thrown
        return Bluebird.try(() => ig.account.login(username, password)).catch(
          IgLoginTwoFactorRequiredError,
          async err => {
            const {username, totp_two_factor_on, two_factor_identifier} = err.response.body.two_factor_info;
            // decide which method to use
            const verificationMethod = totp_two_factor_on ? '0' : '1'; // default to 1 for SMS
            // At this point a code should have been sent
            // Get the code
            const { code } = await inquirer.prompt([
              {
                type: 'input',
                name: 'code',
                message: `Enter code received via ${verificationMethod === '1' ? 'SMS' : 'TOTP'}`,
              },
            ]);
            console.log("Giriş yapılıyor")
            ig.account.twoFactorLogin({
              username,
              verificationCode: code,
              twoFactorIdentifier: two_factor_identifier,
              verificationMethod, // '1' = SMS (default), '0' = TOTP (google auth for example)
              trustThisDevice: '1', // Can be omitted as '1' is used by default
            });
            console.log("Giriş başarılı")
           
          
            
           
            
            
              
          
          } 
          
          
        )
        
      
   
      
      
      

    }
    )
      ();
