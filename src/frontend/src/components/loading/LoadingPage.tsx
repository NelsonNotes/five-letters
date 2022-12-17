import React from 'react'
import { useEffect, useState } from 'react'

import gameLogo from './assets/logo.svg'
import './Loading.css'

export const LoadingPage: React.FC = () => {
	const [count, setCount] = useState(0)

	return (
		<div className='App'>
			<div>
				<img src={gameLogo} className='logo' alt='Game logo' />
			</div>
			<h1>Загрузка . . .</h1>
			<div className='card'>
				<button onClick={() => setCount((count) => count + 1)}>
					Вы накликали {count} раз
				</button>
			</div>
			<p className='read-the-docs'>Пока можно потыкать счетчик</p>
		</div>
	)
}
