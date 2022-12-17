import React, { useState } from 'react'

import './Login.css'
import GameLogo from '../../assets/logo.svg'

import { sessionOperations } from '../../store/session/operations'
import { useAppDispatch } from '../../hooks/app'

export const LoginPage: React.FC = () => {
	const dispatch = useAppDispatch()

	const [username, setUsername] = useState('')
	const [password, setPassword] = useState('')

	const loginHandler = () => {
		dispatch(
			sessionOperations.fetch({
				username,
				password,
				grant_type: 'password',
			})
		)
	}

	return (
		<>
			<div className='App'>
				<div>
					<img src={GameLogo} className='logo' alt='Game logo' />
				</div>
				<h1>Здравствуйте!</h1>
				<h2>Пожалуйста, авторизуйтесь</h2>
				<div className='card'>
					<p>Логин</p>
					<input type='text' onChange={(e) => setUsername(e.target.value)} />
					<p>Пароль</p>
					<input
						type='password'
						onChange={(e) => setPassword(e.target.value)}
					/>
					<br />
					<button type='button' onClick={loginHandler}>
						Войти
					</button>
				</div>
			</div>
		</>
	)
}
